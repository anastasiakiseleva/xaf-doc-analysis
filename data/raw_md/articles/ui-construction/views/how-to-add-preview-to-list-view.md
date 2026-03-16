---
uid: "404210"
title: 'How to: Enable Row Preview Sections in a Grid List Editor'
owner: Anastasiya Kisialeva
---
# How to: Enable Row Preview Sections in a Grid List Editor

[Grid List Editors](xref:113189) can display lengthy memo fields in Row Preview Sections. Use the @DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName property to enable this feature. This property allows you to select one of the columns from the @DevExpress.ExpressApp.Model.IModelListView.Columns collection.

When the @DevExpress.ExpressApp.Model.IModelListView.DataAccessMode property is `DataView`, a list view uses only visible columns to display data in the Row Preview Sections. To customize this behavior, use the @DevExpress.ExpressApp.ListView.CustomizeDisplayableProperties event.

The instructions below customize the **Note** List View. Follow these instructions to enable Row Preview Sections and populate them with values of the `Note.Text` property.

> [!NOTE]
> To follow the steps below, you can use the **MainDemo** application installed as a part of the XAF package. The default location of the application is _%PUBLIC%\Documents\DevExpress Demos <:xx.x:>\\Components\XAF_.
>
> This application's **DemoTask** List View initially displays Preview Sections populated with values of the `DemoTask.Description` property.

1. In the **Solution Explorer**, go to the **MainDemo.Module** project and double-click the _Model.DesignedDiffs.xafml_ file to open it in the [Model Editor](xref:112582).

2. Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **Note** | **Note_ListView** node.

3. Set the @DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName property to `Text`.
	
	![|PreviewColumnName property in the Model Application, DevExpress](~/images/how-to-show-preview-section-in-listview-modelapp.png)

4. Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **Note** | **Note_ListView** | **Columns** | **Text** node.

5. Set the `Index` property to `-1`. This hides the **Text** column from a grid. So, the column values are only displayed in a Row Preview Section.

	![|A column's Index property in the Model Application, DevExpress](~/images/how-to-show-preview-section-in-listview-modelapp-text-property.png)

6. Run the application. Navigate to the **Note** List View to see the preview section.
	
	![|Preview section in Note List View, DevExpress](~/images/how-to-show-preview-section-in-listview-result.png)
