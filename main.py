import matlab.engine

# Change path to where export_BPTF is saved
# import sys
# positionOfPath = 1
    # File location
# r = "C:/Users/ncbrubaker/Documents/export_bptf"
# sys.path.insert( positionOfPath, r)

# Run .m file
eng = matlab.engine.start_matlab()
eng.demo(nargout=0)

print("Hello!")

eng.quit()
