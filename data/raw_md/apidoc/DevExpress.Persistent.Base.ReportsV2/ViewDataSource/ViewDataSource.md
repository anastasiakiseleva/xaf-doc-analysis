---
uid: DevExpress.Persistent.Base.ReportsV2.ViewDataSource
name: ViewDataSource
type: Class
summary: The data source component that retrieves a list of data records (a data view) via the [](xref:DevExpress.ExpressApp.IObjectSpace) without loading complete business classes. Values in each data record can be obtained from specific business class properties directly, or be evaluated by the database server using complex expressions.
syntax:
  content: 'public class ViewDataSource : DataSourceBase, ISortingPropertyDescriptorProvider, ITypedList, IXtraSupportDeserializeCollectionItem'
seealso:
- linkId: DevExpress.Persistent.Base.ReportsV2.ViewDataSource._members
  altText: ViewDataSource Members
---
Use this report data source to create an [](xref:DevExpress.XtraReports.UI.XtraReport) compatible with the [Reports V2 Module](xref:113591). An example is provided in the [Create Predefined Static Reports](xref:113645) topic. The **ViewDataSource** uses the [IObjectSpace.CreateDataView](xref:DevExpress.ExpressApp.IObjectSpace.CreateDataView*) method to load data.

You should explicitly specify the data fields to be loaded via the [ViewDataSource.Properties](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource.Properties) property when using **ViewDataSource**. If you always want to load objects in their entirety, use the [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) component instead.

> [!TIP]
> You can use the [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) component instead of **ViewDataSource**. The difference between these components is described in the [Data Sources for Reports V2](xref:113593) topic.

> [!NOTE]
> [!include[Toolbox_Note](~/templates/toolbox_note111119.md)]