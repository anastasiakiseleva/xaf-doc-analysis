---
uid: "118449"
seealso: []
title: Client Mode
owner: Ekaterina Kiseleva
---
# Client Mode

The default [List View data access mode](xref:113683) is **Client**, which is appropriate in most cases and has no optimization specificities in the case of a large amount of data records.

In **Client** mode, to display a collection of objects, a List View must retrieve all the objects from the [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) and populate the [List Editor](xref:113189) control with them. The more objects exist, the longer it takes for the List View to refresh, even if only a small portion of objects can be displayed in the UI at the same time. Furthermore, the time required to sort and group data also increases proportionally, because the List View has to process all existing objects of the specified type. The use of this mode is fine with a reasonable number of objects in the Collection Source collection. However, in scenarios where their number increases to tens of thousands or more, the List View's performance becomes unacceptable.
