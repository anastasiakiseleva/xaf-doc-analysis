---
uid: "112993"
seealso: []
title: Adjust Data Sources for Reference and Collection Properties
---
# Adjust Data Sources for Reference and Collection Properties

The [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute), [](xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute), and [](xref:DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute) can be applied to [business classes](xref:113664)' [reference](xref:113572) and [collection](xref:113568) properties. These attributes allow adjusting data sources for the following List Views associated with target properties:

| Attribute's Target | Affected List View | Example |
|---|---|---|
| Reference property | List View displayed in a Lookup Property Editor. | [How to: Implement Cascading Filtering for Lookup List Views](xref:112681) |
| Collection property | List View invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) Action in a popup window. | [How to: Filter a Link Dialog's List View](xref:112924) |

Attributes usage:

* The **DataSourceProperty** attribute accepts the name of a collection property to be used as the data source.
* The **DataSourceCriteria** attribute specifies the [criteria expression](xref:4928) used to filter the data source.
* The **DataSourceCriteriaProperty** attribute accepts the name of a [](xref:DevExpress.Data.Filtering.CriteriaOperator) type property which returns data source's filter criteria. This allows you to dynamically apply complex custom filters.

> [!NOTE]
> * When these attributes are applied to a collection property, the collection itself is not filtered. The filter is used for the **Link** Action's popup only.
> * **DataSourceCriteriaProperty** overrides **DataSourceCriteria** when both attributes are applied to the same property.