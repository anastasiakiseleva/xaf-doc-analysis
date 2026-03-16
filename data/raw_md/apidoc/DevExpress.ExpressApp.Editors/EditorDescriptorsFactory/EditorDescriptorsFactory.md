---
uid: DevExpress.ExpressApp.Editors.EditorDescriptorsFactory
name: EditorDescriptorsFactory
type: Class
summary: Provides helper methods used to register View Items, Property Editors, List Editors and their alias names.
syntax:
  content: public class EditorDescriptorsFactory
seealso:
- linkId: DevExpress.ExpressApp.Editors.EditorDescriptorsFactory._members
  altText: EditorDescriptorsFactory Members
---
Generally, you do not need to create new instances of **EditorDescriptorsFactory**. To access the default **EditorDescriptorsFactory** instance, override the **ModuleBase.RegisterEditorDescriptors** protected method and use the _editorDescriptorsFactory_ parameter.

# [C#](#tab/tabid-csharp)

```csharp
protected override void RegisterEditorDescriptors(
    EditorDescriptorsFactory editorDescriptorsFactory) {
    editorDescriptorsFactory.RegisterListEditor(
        typeof(MyBusinessObject), typeof(MyListEditor), true);
}
```
***

To learn more about the **RegisterEditorDescriptor** method, refer to the [](xref:DevExpress.ExpressApp.ModuleBase) class description.