---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate
name: EndUpdate()
type: Method
summary: Resumes List Editor updates (when the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate method pauses updates) and re-renders the Pivot Grid.
syntax:
  content: public void EndUpdate()
seealso: []
---
Enclose your code in the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate - @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate method calls to suppress the List Editor's visual updates and improve its performance when you make multiple changes to the List Editor.

Each call to @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate should be paired with the @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate call. The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.BeginUpdate method locks the component and prevents it from re-rendering after each modification. The @DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EndUpdate method unlocks the control to allow all the changes to be applied.