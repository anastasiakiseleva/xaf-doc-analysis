---
uid: DevExpress.Persistent.Base.ReportsV2.CollectionDataSource
name: CollectionDataSource
type: Class
summary: The data source component that loads a collection of business objects via the [](xref:DevExpress.ExpressApp.IObjectSpace).
syntax:
  content: 'public class CollectionDataSource : DataSourceBase, ISortingPropertyDescriptorProvider, ITypedList'
seealso:
- linkId: DevExpress.Persistent.Base.ReportsV2.CollectionDataSource._members
  altText: CollectionDataSource Members
---
Use this report data source to create an [](xref:DevExpress.XtraReports.UI.XtraReport) compatible with the [Reports V2 Module](xref:113591). An example is provided in the [Create Predefined Static Reports](xref:113645) topic. The **CollectionDataSource** uses the [IObjectSpace.CreateCollection](xref:DevExpress.ExpressApp.IObjectSpace.CreateCollection*) method to load data.

Use **CollectionDataSource** when you do not need to display a large amount of data, because this component loads objects in their entirety, including fields that are not displayed in the report. If you experience performance issues, use [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) instead, and explicitly specify the required fields via the [ViewDataSource.Properties](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource.Properties) collection.

> [!TIP]
> You can use the [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) component instead of **CollectionDataSource**. The difference between these components is described in the [Data Sources for Reports V2](xref:113593) topic.

> [!NOTE]
> [!include[Toolbox_Note](~/templates/toolbox_note111119.md)]