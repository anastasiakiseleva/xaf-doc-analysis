---
uid: DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterPropertyEditorAlias(System.String,System.Type,DevExpress.ExpressApp.Editors.IsMemberCompatibleHandler)
name: RegisterPropertyEditorAlias(String, Type, IsMemberCompatibleHandler)
type: Method
summary: Registers a [Property Editor](xref:112612)'s alias name and specifies the handler which provides a logic to choose if the alias is appropriate for the given property.
syntax:
  content: public void RegisterPropertyEditorAlias(string aliasName, Type propertyType, IsMemberCompatibleHandler memberHandler)
  parameters:
  - id: aliasName
    type: System.String
    description: A string specifying the Property Editor's alias name.
  - id: propertyType
    type: System.Type
    description: A [](xref:System.Type) object specifying the target property type.
  - id: memberHandler
    type: DevExpress.ExpressApp.Editors.IsMemberCompatibleHandler
    description: The **IsMemberCompatibleHandler** object which allows you to choose if the _aliasName_ is appropriate for the _propertyType_.
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase
---
The _classHandler_ parameter is used if you want to register a number of editors for one type and choose the appropriate editor according to the logic implemented in it.

# [C#](#tab/tabid-csharp)

```csharp
public class MyModule : ModuleBase {
    //...
    protected override void RegisterEditorDescriptors(EditorDescriptorsFactory 
    editorDescriptorsFactory) {
        //... 
        editorDescriptorsFactory.RegisterPropertyEditorAlias("CustomPropertyEditorAlias", 
        typeof(DateTime), IsMemberCompatibleHandler);
    }
    private static bool IsMemberCompatibleHandler(IModelMember modelMember) {
        //...
    }
}
```
***