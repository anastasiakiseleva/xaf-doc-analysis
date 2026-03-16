---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetClassCaption(System.String)
name: GetClassCaption(String)
type: Method
summary: Returns the display caption corresponding to a [business class](xref:112570).
syntax:
  content: public static string GetClassCaption(string classFullName)
  parameters:
  - id: classFullName
    type: System.String
    description: A string representing the fully-qualified name of a business class.
  return:
    type: System.String
    description: A string representing the display caption corresponding to the specified business class.
seealso: []
---
For business classes used in an **XAF** application, this method returns the [IModelClass.Caption](xref:DevExpress.ExpressApp.Model.IModelClass.Caption) property value of the corresponding **Class** node. For all the other classes, the **GetClassCaption** method returns the fully-qualified name of the class.