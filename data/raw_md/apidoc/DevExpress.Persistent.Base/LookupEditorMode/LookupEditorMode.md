---
uid: DevExpress.Persistent.Base.LookupEditorMode
name: LookupEditorMode
type: Enum
summary: Specifies the mode of a business class property's Lookup Property Editor.
syntax:
  content: public enum LookupEditorMode
seealso: []
---
`LookupEditorMode` enumeration specifies several aspects of Lookup Property Editor behavior: 

- Data loading mode
- Text search capabilities
- Editor UI type

## Specify Lookup Property Editor Mode in the Model Editor

[IModelClass.DefaultLookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultLookupEditorMode)
:   Specifies the default mode for all Lookup Property Editors bound to reference properties of the current type (**BOModel | \<Class\>**).
[IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode)
:   Specifies the mode of the current Lookup Property Editor (**BOModel | \<Class\> | \<Class\>_DetailView | Items | \<Item\>**).

## Specify Lookup Property Editor Mode in Code

Apply the [LookupEditorModeAttribute](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute) to a reference property to specify the editor mode:

[!include[](~/templates/lookupeditormodeattribute-example.md)]

For more information about search capabilities in [LookupPropertyEditor](xref:113572), its data retrieval modes and corresponding UI options, refer to the following topic: [How to: Add Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925).