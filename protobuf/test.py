import test2_pb2
  
testinfo = test2_pb2.testinfo()  
testinfo.devtype = 100  
testinfo.devid = 2  
testinfo.unitid = 3  
testinfo.chlid = 4  
testinfo.testid = 250
testinfo.stepdata = b'abd'

print(testinfo, testinfo.devtype)  
out = testinfo.SerializeToString()  
print(out)  
  
  
decode = test2_pb2.testinfo()  
decode.ParseFromString(out)  
  
print(decode)