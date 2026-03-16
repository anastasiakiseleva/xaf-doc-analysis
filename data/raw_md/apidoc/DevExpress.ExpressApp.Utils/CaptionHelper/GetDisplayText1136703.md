---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.GetDisplayText(System.Object)
name: GetDisplayText(Object)
type: Method
summary: Returns the value of the specified object's default member.
syntax:
  content: public static string GetDisplayText(object theObject)
  parameters:
  - id: theObject
    type: System.Object
    description: An object for which a display text is generated.
  return:
    type: System.String
    description: A string that is the value of the default member.
seealso: []
---
To generate a display text for an object, the value of its default member (see [ITypeInfo.DefaultMember](xref:DevExpress.ExpressApp.DC.ITypeInfo.DefaultMember)) is retrieved. This value is formatted according to the format specified by the [IModelClass.ObjectCaptionFormat](xref:DevExpress.ExpressApp.Model.IModelClass.ObjectCaptionFormat) property of the Application Model's **BOModel** | **_\<Class\>_** node.