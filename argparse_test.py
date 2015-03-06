import argparse 
  
parser = argparse.ArgumentParser(description="CDR Report")
parser.add_argument("-r", '--run', action='store', dest='run_type', help='Run type', choices={'auto', 'manual'}, default='auto')
parser.add_argument("-s", "--start", action="store", dest='start_time', help="Start time")
parser.add_argument("-e", "--end", action="store", dest='end_time', help="End time")
args = parser.parse_args()
print (args)
