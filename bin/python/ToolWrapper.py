import ToolBox

class Tool(object):
 tool_name_ = ""
 
 def __init__(self, str):
  self.tool_name_ = str
 
 def __getattr__(self, name):
  try:
   return ToolBox.toolGetVariable(self.tool_name_, name)
  except:
   def method(*args):
    ToolBox.toolFunction(self.tool_name_, name, args)
   return method
   
 def __setattr__(self, name, value):
  ToolBox.toolSetVariable(self.tool_name_, name, value )
  super().__setattr__(name, value)
 
 def __dir__(self):
  return ToolBox.toolGetFunctions(self.tool_name_) + ToolBox.toolGetVariables(self.tool_name_)
  
class Item(object):
 item_name_ = ""

 def __new__(cls, str):
  if ToolBox.itemGetFunctions(str) == None:
   print("Toolbox Item not found '" + str + "'")
   return None
  return super(Item, cls).__new__(cls)
			
 def __init__(self, str):
  self.item_name_ = str
  
 def __getattr__(self, name):
  try:
   return ToolBox.itemGetVariable(self.item_name_, name)
  except:
   def method(*args):
    ToolBox.itemFunction(self.item_name_, name, args)
   return method
   
 def __setattr__(self, name, value):
  ToolBox.itemSetVariable(self.item_name_, name, value )
  super().__setattr__(name, value)
 
 def __dir__(self):
  return ToolBox.itemGetFunctions(self.item_name_) + ToolBox.itemGetVariables(self.item_name_)
  
 
RaytracerTool = Tool("RaytracerTool")
BaseTool = Tool("BaseTool")
RelightingWizardTool = Tool("RelightingWizardTool")
