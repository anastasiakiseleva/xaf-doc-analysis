---
uid: DevExpress.ExpressApp.LookupEditPropertyCollectionSource
name: LookupEditPropertyCollectionSource
type: Class
summary: The Collection Source used for the List Views created by Lookup Property Editors.
syntax:
  content: 'public class LookupEditPropertyCollectionSource : PropertyCollectionSource'
seealso:
- linkId: DevExpress.ExpressApp.LookupEditPropertyCollectionSource._members
  altText: LookupEditPropertyCollectionSource Members
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor
---
In **XAF**, by default, reference properties are displayed in a UI via [Lookup Property Editors](xref:113014). To display a drop-down list of the possible property values, a Lookup Property Editor creates a [List View](xref:112611). 
List Views of this kind use instances either of the [](xref:DevExpress.ExpressApp.CollectionSource) class or of the **LookupEditPropertyCollectionSource** class as the data sources. The letter is used when the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) is applied to the reference property. In all other scenarios, an instance of the **CollectionSource** class is used as a data source.

The **LookupEditPropertyCollectionSource** is also used as the data source by List Views invoked via the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) to edit a collection property that has the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) applied to it.

Compared to the [](xref:DevExpress.ExpressApp.PropertyCollectionSource), the **LookupEditPropertyCollectionSource** introduces the additional [LookupEditPropertyCollectionSource.LookupMode](xref:DevExpress.ExpressApp.LookupEditPropertyCollectionSource.LookupMode) property, whose value can be used to determine the kind of List View that uses the **LookupEditPropertyCollectionSource**. The **LookupMode** property may return one of the two **LookupEditCollectionSourceMode** enumeration's values:

* [LookupEditCollectionSourceMode.Lookup](xref:DevExpress.ExpressApp.LookupEditCollectionSourceMode.Lookup) - the Collection Source is used by a Lookup Property Editor's List View.
* [LookupEditCollectionSourceMode.Link](xref:DevExpress.ExpressApp.LookupEditCollectionSourceMode.Link) - the Collection Source is used by a List View invoked via the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction).

LookupEditPropertyCollectionSource can only be created in client mode, because it is used for List Views that display a particular set of objects specified by a property (see [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute)).