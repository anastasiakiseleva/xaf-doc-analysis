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
# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Collections.Generic
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Utils
' ...
Public NotInheritable Partial Class MySolutionWinModule
	Inherits ModuleBase
	Public Sub New()
		' ...
		DataAccessModeHelper.RegisterEditorSupportedModes(GetType(CustomListEditor), 
        New List(Of CollectionSourceDataAccessMode) _
        From {CollectionSourceDataAccessMode.Client, CollectionSourceDataAccessMode.Server})
	End Sub
	' ...
End Class
```

***