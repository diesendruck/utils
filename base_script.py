import argparse
import os
from datetime import datetime
from pathlib import Path

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='')
    parser.add_argument('--output_dir', type=str, default='output')
    args = parser.parse_args()
    return args

def main(args):
    pass

if __name__ == '__main__':
    args = argparser()
  
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    args.output_dir = os.path.join(args.output_dir, time)
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
  
    main(args)
  
