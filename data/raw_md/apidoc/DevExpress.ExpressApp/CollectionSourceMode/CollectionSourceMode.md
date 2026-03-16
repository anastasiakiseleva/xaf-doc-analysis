---
uid: DevExpress.ExpressApp.CollectionSourceMode
name: CollectionSourceMode
type: Enum
summary: Contains values that specify modes of operation for Collection Sources.
syntax:
  content: public enum CollectionSourceMode
seealso: []
---
These enumeration values are used to specify the [CollectionSourceBase.Mode](xref:DevExpress.ExpressApp.CollectionSourceBase.Mode) and [CollectionSourceModeAttribute.Mode](xref:DevExpress.ExpressApp.CollectionSourceModeAttribute.Mode) properties.

[comment]: <> (<\!--<para>)
[comment]: <> (Collection Sources have two modes of operation - <b>Normal</b> and <b>Proxy</b>. Suppose you have filtered a List View via the <see cref="T:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute"/>. In <b>Normal</b> mode, if you iterate over the collection represented by the List View, you will only see the filtered objects. This is because, in this mode, when the Collection Source's collection is filtered, the corresponding criteria is directly applied to the collection. In <b>Proxy</b> mode, the criteria is not directly applied to the object collection. Instead, an intermediate proxy collection is created, and the filter criteria is applied to it. So, in this mode, the underlying collection is unaffected, and if you iterate over it, you will see all objects belonging to the collection.)
[comment]: <> (</para>)
[comment]: <> (-->)

> [!NOTE]
> A Collection Source's mode of operation does not affect control-specific filtering features. For instance, the **GridControl** used by the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor), allows end-users to filter data via the auto filter row and filter panel. When end-users use these features, filtering is performed on the control level, and is not reflected in the Collection Source.