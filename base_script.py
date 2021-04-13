import argparse
import os
from datetime import datetime
from pathlib import Path

def argparse():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str, default='')
  parser.add_argument('--output_dir', type=str, default='output')
  args = parser.parse_args()
  return args

def main(args):
  pass

if __name__ == '__main__':
  args = argparse()
  
  time = datetime.now().strftime('%Y%m%d%H%M%S')
  args.out_dir = os.path.join(args.out_dir, time)
  Path(args.out_dir).mkdir(parents=True, exist_ok=True)
  
  main(args)
  
