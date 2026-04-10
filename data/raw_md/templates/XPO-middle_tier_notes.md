* The `OnSaving` and `OnDeleting` methods of a business class can be called multiple times because [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core) and [Middle Tier Security](xref:113439) use more than one `Session`/`DbContext` object. If you implement custom logic in these methods, check whether a new value is already assigned to a property. This helps you avoid incorrect results. The following article describes how to do this with XPO: [](xref:403711).
* Detail Views do not display changes made to an object within a transaction (for example, [an auto-generated sequential number for an XPO business object](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction)) even if you saved this object in a View. These changes are made on the server only and are not automatically passed to the client application. To show these changes, reload the object. If you want to reload the object on each Save operation, override the business class's `OnSaved` method. The following example demonstrates how to override this method to reload an object on the client: 

    ```csharp
    using DevExpress.Persistent.BaseImpl;
    // ...
    public class DemoObject : BaseObject {
        // ...
        protected override void OnSaved() {
            base.OnSaved();
            // 0 is the default value
            if (Number == 0) {
                Session.Reload(this);
            }
        }
    }
    ```

* The [Session.DataLayer](xref:DevExpress.Xpo.Session.DataLayer) property is _null_ in the secured `Session`. Instead of `DataLayer`, we recommend that you use the [View.ObjectSpace](xref:DevExpress.ExpressApp.View.ObjectSpace) property to query and change data from the database. This technique is also recommended for non-secure applications.

    If this recommendation does not apply to your scenario, use the [Session.ObjectLayer](xref:DevExpress.Xpo.Session.ObjectLayer) property instead of `DataLayer`.
    
    You can also execute different code on the server and client depending on the `DataLayer` and `ObjectLayer` property values. The following example demonstrates how to do it: 

    ```csharp
    using DevExpress.ExpressApp.Security.ClientServer;
    using DevExpress.Persistent.BaseImpl;
    // ...
    public class DemoObject : BaseObject {
        // ...
        protected override void OnSaving() { 
            if(Session.DataLayer != null && !(Session.ObjectLayer is SecuredSessionObjectLayer)) { 
                // Server-side code
            } 
            else {  
                // Client-side code 
            } 
            base.OnSaving(); 
        }
    }
    ```
