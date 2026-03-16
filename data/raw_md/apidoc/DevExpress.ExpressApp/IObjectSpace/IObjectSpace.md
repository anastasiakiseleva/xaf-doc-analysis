---
uid: DevExpress.ExpressApp.IObjectSpace
name: IObjectSpace
type: Interface
summary: Declares members implemented by [Object Space](xref:113707).
syntax:
  content: 'public interface IObjectSpace : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace._members
  altText: IObjectSpace Members
---
For more information on the Object Space concept, refer to the following class description: [](xref:DevExpress.ExpressApp.BaseObjectSpace).

Follow the steps below to implement a custom Object Space:
1. Create a new [](xref:DevExpress.ExpressApp.BaseObjectSpace) descendant. **BaseObjectSpace** implements the **IObjectSpace** members that are not related to the data layer. 
2. Override **BaseObjectSpace**'s protected virtual methods you want to customize.
3. Implement the **IObjectSpace** members related to the data layer.

You can also inherit one of the [](xref:DevExpress.ExpressApp.BaseObjectSpace) descendants. 

The following article demonstrates how to create a custom Object Space class and register the custom Object Space Provider for it: [How to customize the Object Space behavior in XPO-based XAF applications](xref:405388).

The following example demonstrates how to use the **IObjectSpace** methods:

[!include[](~/templates/objectspace-snippets.md)]
