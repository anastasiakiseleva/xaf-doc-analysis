---
uid: DevExpress.ExpressApp.Blazor.SystemModule.BlazorExportController.ExportVisibleColumnsOnly
name: ExportVisibleColumnsOnly
type: Field
summary: Specifies whether hidden columns should be exported.
syntax:
  content: |-
    [Browsable(false)]
    public static bool ExportVisibleColumnsOnly
  return:
    type: System.Boolean
    description: '`true` to export only visible columns; `false` to export both visible and hidden columns.'
seealso: []
defaultMemberValue: 'true'
---
Set the `ExportVisibleColumnsOnly` to `false` to export hidden columns.

```csharp
public class HiddenExportController : ObjectViewController<ListView, Review> {

protected override void OnActivated() {
    base.OnActivated();
    BlazorExportController.ExportVisibleColumnsOnly = false;
}

protected override void OnDeactivated() {
    BlazorExportController.ExportVisibleColumnsOnly = true;
    base.OnDeactivated();
}
```