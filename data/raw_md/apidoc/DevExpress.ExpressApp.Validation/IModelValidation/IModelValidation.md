---
uid: DevExpress.ExpressApp.Validation.IModelValidation
name: IModelValidation
type: Interface
summary: The Validation node defines Contexts and Rules used in your application.
syntax:
  content: |-
    [ImageName("BO_Validation")]
    public interface IModelValidation : IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Validation.IModelValidation._members
  altText: IModelValidation Members
- linkId: "113684"
- linkId: "112579"
- linkId: "112580"
---
The Validation node allows setting Rules for objects and their properties without implementing code. Generally, if using the Validation System in your application, it is recommended that you do it in code via attributes. However, providing access to this feature in the [Model Editor](xref:112582) allows administrators and end-users to edit Rules and Contexts.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.