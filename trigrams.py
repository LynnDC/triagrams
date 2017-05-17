def main(file, x):
    read_file  = open(file).read()


  output = []
  for i in range(len(input)-n+1):
    output.append(input[i:i+n])
  return output

[' '.join(x) for x in ngrams('a b c d', 2)]
