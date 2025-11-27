def create_codon_dict(file_path):
  codon_dict = {}
  for line in lines:
    line = line.strip()
    cells = line.split('\t')
    key = cells [0]
    value = cells [2]
    codon_dict.update ({key:value})
  return codon_dict


