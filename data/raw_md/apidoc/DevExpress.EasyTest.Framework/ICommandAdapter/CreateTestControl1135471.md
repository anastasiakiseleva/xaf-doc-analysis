---
uid: DevExpress.EasyTest.Framework.ICommandAdapter.CreateTestControl(System.String,System.String)
name: CreateTestControl(String, String)
type: Method
summary: Finds the specific control and creates the test control for it.
syntax:
  content: ITestControl CreateTestControl(string controlType, string name)
  parameters:
  - id: controlType
    type: System.String
    description: A string that specifies the test control types. Valid types can be obtained from the [](xref:DevExpress.EasyTest.Framework.TestControlType) class' constants.
  - id: name
    type: System.String
    description: A sting that is the control caption.
  return:
    type: DevExpress.EasyTest.Framework.ITestControl
    description: An [](xref:DevExpress.EasyTest.Framework.ITestControl) object that is the created test control.
seealso: []
---
To see this method in use, refer to the [How to: Implement a Custom EasyTest Command](xref:113340) topic.