---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate
name: BeginUpdate()
type: Method
summary: Suspends List Editor updates caused by parameter changes and method calls until the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate method is called.
syntax:
  content: public void BeginUpdate()
seealso: []
---
Enclose your code in the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate - @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate method calls to suppress visual updates and improve performance when you make multiple changes to the List Editor.

Each call to @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate should be paired with the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate call. The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate method locks the component to prevent it from re-rendering after each modification. The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate method unlocks the control to allow all the changes to be applied.