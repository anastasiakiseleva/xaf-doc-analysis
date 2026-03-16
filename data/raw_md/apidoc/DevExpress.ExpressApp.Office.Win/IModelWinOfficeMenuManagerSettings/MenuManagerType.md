---
uid: DevExpress.ExpressApp.Office.Win.IModelWinOfficeMenuManagerSettings.MenuManagerType
name: MenuManagerType
type: Property
summary: Specifies the type of menu displayed in [office controls](xref:400003).
syntax:
  content: |-
    [ModelBrowsable(typeof(OfficeModelMenuManagerVisibilityCalculator))]
    DefaultMenuManagerType MenuManagerType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Office.Win.DefaultMenuManagerType
    description: The menu type.
seealso:
- linkId: "400004"
---
The `MenuManagerType` property specifies the Menu Manager type for [office controls](xref:400003): Rich Text Editor, Spreadsheet, or PDF Viewer.

To specify the menu type, open the _Model.xafml_ file in the _MySolution.Win_ project. In the [Model Editor](xref:112582), navigate to the **Views | {MySolution}.Module.BusinessObjects | {ClassName} | {ClassName}_Detail View | Items | {ItemName}** node and specify the `MenuManagerType` property value.

![Menu Type Setup in Model Editor, DevExpress](~/images/xaf-win-menu-manager-type-in-model-editor.png)
