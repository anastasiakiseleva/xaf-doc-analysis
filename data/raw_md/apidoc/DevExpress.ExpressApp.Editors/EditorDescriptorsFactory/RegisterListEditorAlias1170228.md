---
uid: DevExpress.ExpressApp.Editors.EditorDescriptorsFactory.RegisterListEditorAlias(System.String,System.Type,DevExpress.ExpressApp.Editors.IsClassCompatibleHandler)
name: RegisterListEditorAlias(String, Type, IsClassCompatibleHandler)
type: Method
summary: Registers a [List Editor](xref:113189)'s alias name and specifies the handler which provides a logic to choose if the alias is appropriate for the given type.
syntax:
  content: public void RegisterListEditorAlias(string aliasName, Type elementType, IsClassCompatibleHandler classHandler)
  parameters:
  - id: aliasName
    type: System.String
    description: A string specifying the List Editor's alias name.
  - id: elementType
    type: System.Type
    description: A [](xref:System.Type) object specifying the List Editor's target type.
  - id: classHandler
    type: DevExpress.ExpressApp.Editors.IsClassCompatibleHandler
    description: The **IsClassCompatibleHandler** object which allows you to choose if the _aliasName_ is appropriate for the _elementType_.
seealso:
- linkId: DevExpress.ExpressApp.ModuleBase
---
The _classHandler_ parameter is used if you want to register a number of editors for one type and choose the appropriate editor according to the logic implemented in it. In different situations, the editor satisfying the conditions will be applied to current type first.

# [C#](#tab/tabid-csharp)

```csharp
public class MyModule : ModuleBase {
    //...
    protected override void RegisterEditorDescriptors(EditorDescriptorsFactory 
    editorDescriptorsFactory) {
        //...
        editorDescriptorsFactory.RegisterListEditorAlias("MyAlias", typeof(object), 
        IsCriteriaProperty); 
    }
    private static bool IsCriteriaProperty(IModelClass modelClass) {
        //...    
    }
}
```
***