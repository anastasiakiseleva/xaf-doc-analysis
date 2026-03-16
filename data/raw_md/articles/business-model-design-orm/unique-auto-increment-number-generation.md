---
uid: "403605"
title: 'Auto-Generate Unique Number Sequence'
owner: Eugenia Simonova
seealso:
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t639653/web-how-to-avoid-issues-with-data-bound-controls-due-to-missing-or-non-unique-key-values#
  altText: Web - How to avoid issues with data-bound controls due to missing or non-unique key values
---
# Auto-Generate Unique Number Sequence

Orders, Invoices, Articles, and other business entities often require an auto-filled Number or Code field that users can memorize. Although these user-friendly field values are sequential, gaps are permitted (for example, when a user deletes an order).
Use one of the following techniques to use this field in XAF applications:

[Database-Level: Auto-Increment Database Column](#database-level-auto-increment-database-column)
:   This solution avoids sequence gaps. Since this solution is implemented at the database level, it is specific to the database type.
[ORM-Level: Programmatic Transaction (XPO Only)](#orm-level-programmatic-transaction-xpo-only)
:   This solution is more complicated and implemented at the ORM level. It does not depend on the database type and also avoids sequence gaps.

## Database-Level: Auto-Increment Database Column

### EF Core

Use the following steps to generate sequential values for business object properties to ensure that these properties are assigned a value when their respective objects are saved to the database:

1. Add the `[DatabaseGenerated(DatabaseGeneratedOption.Identity)]` attribute to the required business object property:

   ```csharp
   public class Address : BaseObject {
       // ...
       [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
       public virtual long SequentialNumber { get; set; }
       // ...
   }
   ```

2. Add the following code snippet to the DbContext's `OnModelCreating` method implementation to ensure that the generated values are always displayed in the UI immediately after the object has been saved:

   ```csharp
   public class GenerateUserFriendlyIdEFCoreDbContext : DbContext {
       // ...
       protected override void OnModelCreating(ModelBuilder modelBuilder) {
           // ...
           modelBuilder.Entity<Address>().UsePropertyAccessMode(PropertyAccessMode.FieldDuringConstruction);
       }
   }
   ```

[!example[XAF - How to generate a sequential number for a persistent object within a database transaction with Entity Framework Core](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction)] 

### XPO

Use the [FetchOnly](xref:DevExpress.Xpo.FetchOnlyAttribute) attribute as follows:

1. Create an auto-increment database column (for example, [Identity](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-transact-sql-identity-property) in SQL Server).
2. Create a persistent property mapped to this column and decorate it with the `FetchOnly` attribute.

## ORM-Level: Programmatic Transaction (XPO Only)

The following example shows how to implement the Programmatic Transaction solution: 

[!example[XAF - How to generate a sequential number for a persistent object within a database transaction with XPO](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction/tree/HEAD/CS/XPO)] 

### Refresh the Identifier Field Value in the UI

If you use the **Programmatic Transaction** solution with [UI-Level](xref:113436#ui-level-mode) security, an application displays the identifier field value immediately after a user creates a new object. In the [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core) and [Middle-Tier Application Server](xref:113439) configuration, the newly generated sequence number is displayed only after a manual refresh. XAF does not pass the sequence to the client immediately. Implement one of the techniques described below to refresh the field value automatically.

#### Override the Business Class OnSaved Method

Override your business class `OnSaved` method to update the value on the client side:
# [C#](#tab/tabid-csharp)
 
```csharp
namespace MySolution.Module.BusinessObjects {  
    public class YourBusinessClass : YourBaseXpoClass {  
        // ...  
        protected override void OnSaved() {  
            base.OnSaved();  
            if(Number == 0) { //  0 is the default value of the sequence number property.
                Session.Reload(this);  
            }  
        }  
        // ...  
    }  
}  
```
***

#### Use a Custom Controller to Reload the Object Space

Use a custom Controller to reload the [Object Space](xref:113707) after new objects are saved:

# [C#](#tab/tabid-csharp)
 
```csharp
namespace MySolution.Module.Controllers {  
    // ...  
    public class RefreshAfterCommitController : ViewController {  
        bool needRefresh = false;  
        public RefreshAfterCommitController() {  
            TargetViewNesting = Nesting.Root;  
        }  
        protected override void OnActivated() {  
            base.OnActivated();  
            ObjectSpace.Committed += ObjectSpace_Committed;  
            ObjectSpace.Committing += ObjectSpace_Committing;  
            ObjectSpace.Reloaded += ObjectSpace_Reloaded;  
        }  
        protected override void OnDeactivated() {  
            ObjectSpace.Committed -= ObjectSpace_Committed;  
            ObjectSpace.Committing -= ObjectSpace_Committing;  
            ObjectSpace.Reloaded -= ObjectSpace_Reloaded;  
            base.OnDeactivated();  
        }  
        private void ObjectSpace_Reloaded(object sender, EventArgs e) {  
            needRefresh = false;  
        }  
        private void ObjectSpace_Committing(object sender, System.ComponentModel.CancelEventArgs e) {  
            var objectSpace = (IObjectSpace)sender;  
            foreach (var obj in objectSpace.GetObjectsToSave(false)) {  
                if (objectSpace.IsNewObject(obj)) {  
                    needRefresh = true; break;  
                }  
            }  
        }  
        private void ObjectSpace_Committed(object sender, EventArgs e) {  
            if (needRefresh) {  
                ((IObjectSpace)sender).Refresh();  
                needRefresh = false;  
            }  
        }  
    }  
}  
```
***
