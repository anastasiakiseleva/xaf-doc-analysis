`DataAccessMode`'s combo box displays only modes that are compatible with the selected List Editor (a node's @DevExpress.ExpressApp.Model.IModelListView.EditorType property). If you use a custom List Editor, specify its supported modes in the static `DataAccessModeHelper.RegisterEditorSupportedModes` method. Call this method from code executed at design time before the Model Editor is loaded (for example, from a Module's constructor). Pass the List Editor's type and a list of supported modes to this method. Otherwise, the Model Editor shows all modes for this List Editor.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.Generic;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Utils;
// ...
public sealed partial class MySolutionWinModule : ModuleBase {
    public MySolutionWinModule() {
        // ...
        DataAccessModeHelper.RegisterEditorSupportedModes(typeof(CustomListEditor), 
        new List<CollectionSourceDataAccessMode> { CollectionSourceDataAccessMode.Client, CollectionSourceDataAccessMode.Server });
    }
    // ...
}
```
***