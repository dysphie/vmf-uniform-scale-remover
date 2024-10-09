import re
import subprocess
import os
import sys
from dotenv import load_dotenv

load_dotenv()

crowbar_path = os.getenv('CROWBAR_PATH')
assets_path = os.getenv('ASSETS_PATH')

def get_suffix(scale):
	return '_s' + str(scale).replace('.', '_')

def recompile_model(mdl_path, scale):
	suffix = get_suffix(scale)
	qc_name = mdl_path.split('/')[-1].replace('.mdl', '.qc')

	print(f'{crowbar_path} {mdl_path}')
	subprocess.run([crowbar_path, 
		'-p', mdl_path,
		'-o', './scaled_qcs'
	])
	
	with open('./scaled_qcs/' + qc_name, 'r+') as qc:
		content = [f'$scale {scale}\n']
		for line in qc.readlines():
			if '$bbox' in line:
				line = f'// {line}'
			elif '$modelname' in line:
				line = line.replace('.mdl', f'{suffix}.mdl')
			content.append(line)
		qc.seek(0)
		qc.truncate()
		qc.writelines(content)

def process_vmf(vmf_path):

	output_path = vmf_path.replace('.vmf', '_descaled.vmf')

	model = None
	model_line = None

	with open(vmf_path, 'r') as f:
		lines = f.readlines()

		for cur_line, line in enumerate(lines):

			model_match = re.match(r'\s*"model"\s*"(.+)"', line)
			if model_match:
				print('found model ' + line)
				model = model_match.group(1)
				model_line = cur_line
		
			scale_match = re.match(r'\s*"uniformscale"\s*"([^1].*)"', line)
			if scale_match:
				scale = scale_match.group(1)
				
				recompile_model(f'{assets_path}/{model}', scale)

				suffix = get_suffix(scale)
				lines[model_line] = lines[model_line].replace('.mdl', f'{suffix}.mdl')
				lines[cur_line] = '\t"uniformscale" "1"\n'
	
	with open(output_path, 'w') as f:
		f.writelines(lines)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		sys.exit(1)

	vmf_path = sys.argv[1]
	process_vmf(vmf_path)
