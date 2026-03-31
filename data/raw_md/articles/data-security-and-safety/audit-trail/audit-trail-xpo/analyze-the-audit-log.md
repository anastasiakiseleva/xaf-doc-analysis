---
uid: "113615"
title: Analyze the Audit Log
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-show-audit-entries-for-a-current-object-and-its-aggregated-objects-in-one-list
  altText: XAF - How to show audit entries for a current object and its aggregated objects in one list
---
# Analyze the Audit Log

You can access the audit log externally using any database management system (DBMS) that supports SQL query execution. If you are using Microsoft SQL Server, **Microsoft SQL Server Management Studio** is recommended. You can also use the [SQLCMD console tool](https://learn.microsoft.com/en-us/previous-versions/sql/sql-server-2008-r2/ms165702(v=sql.105)) to execute SQL queries, but it will be much less convenient.

## Analyze the Audit Log using SQL Queries
You can write various SQL queries to access data from the audit log that is stored in the database. A common query template may look like the following:

```
select OperationType, ModifiedOn, UserName, PropertyName, DisplayName, OldValue, NewValue
from AuditDataItemPersistent a
join AuditedObjectWeakReference aw on a.AuditedObject = aw.Oid
```

For example, to filter all changes of a particular object, use the following SQL statement (for Microsoft SQL):

```
select OperationType, ModifiedOn, UserName, PropertyName, DisplayName, OldValue, NewValue
from AuditDataItemPersistent a
join AuditedObjectWeakReference aw on a.AuditedObject = aw.Oid
where PropertyName = 'Office' and aw.GuidId = '7F184C67-AE6C-4E79-B2E8-189494E51452'
order by ModifiedOn
```

If the type of the primary key field is INT, rather than GUID, use the **AuditedObjectWeakReference** table's **IntId** field, instead of the **GuidId** field, to join the tables in the query above.

## Analyze the Audit Log in a UI

> [!IMPORTANT]
> This log does not consider [Member Permissions](xref:404633#navigation-permissions). To hide property values from the log, configure permissions for the `AuditDataItemPersistent` class accordingly.

The current version of the **Audit Trail** module does not allow representing the audit log in the user interface without modifying business object implementation. So, if you want to view the changes made with a particular object, add an **AuditTrail** collection property that lists objects from the audit log. The following code demonstrates this.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp;
// ...
[DefaultClassOptions]
public class MyBusinessObject : BaseObject {
    public MyBusinessObject(Session session) : base(session) { }
    //...
    private XPCollection<AuditDataItemPersistent> auditTrail;
    [CollectionOperationSet(AllowAdd = false, AllowRemove = false)]
    public XPCollection<AuditDataItemPersistent> AuditTrail {
        get {
            if(auditTrail == null) {
               auditTrail = AuditedObjectWeakReference.GetAuditTrail(Session, this);
            }
            return auditTrail;
        }
    }
}
```
***

The following image shows a Detail View that contains the **AuditTrail** property demonstrated in the code above.

![AuditTrail Win](~/images/audittrail-wiin115417.png)

## Purge the Audit Log using SQL Queries
The following SQL statements illustrate how to delete all audit log entries made prior to October 24, 2018.

```
update [AuditDataItemPersistent]
set
  GCRecord = 1, AuditedObject = null
where ModifiedOn < '2018-10-24'

update [XPWeakReference]
set
  GCRecord = 1
where Oid in (select NewObject from AuditDataItemPersistent where GCRecord is not null) or
   Oid in (select OldObject from AuditDataItemPersistent where GCRecord is not null) or
   (Oid in (select Oid from AuditedObjectWeakReference) and
    not (Oid in (select AuditedObject from AuditDataItemPersistent where AuditedObject is not null)))

delete from AuditDataItemPersistent
where GCRecord is not null

delete from AuditedObjectWeakReference
where Oid in (select Oid from [XPWeakReference] where GCRecord is not null)

delete from [XPWeakReference]
where GCRecord is not null
```

You can implement an [Action](xref:112622), available only to administrators, that will execute the above statements using standard ADO.NET approaches.
