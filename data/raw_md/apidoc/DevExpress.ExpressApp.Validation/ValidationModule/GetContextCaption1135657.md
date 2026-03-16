---
uid: DevExpress.ExpressApp.Validation.ValidationModule.GetContextCaption(System.String,DevExpress.ExpressApp.Model.IModelApplication)
name: GetContextCaption(String, IModelApplication)
type: Method
summary: Retrieves the caption associated with a particular validation context.
syntax:
  content: public static string GetContextCaption(string contextId, IModelApplication modelApplication)
  parameters:
  - id: contextId
    type: System.String
    description: A string representation of a context identifier whose associated caption must be retrieved.
  - id: modelApplication
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object, which is the root node of the [Application Model](xref:112580).
  return:
    type: System.String
    description: A string containing the caption associated with the _contextId_ validation context.
seealso:
- linkId: "113010"
---
Generally, you do not need to use this method.