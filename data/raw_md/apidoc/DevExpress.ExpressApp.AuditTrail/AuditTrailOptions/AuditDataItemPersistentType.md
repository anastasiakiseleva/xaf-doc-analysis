---
uid: DevExpress.ExpressApp.AuditTrail.AuditTrailOptions.AuditDataItemPersistentType
name: AuditDataItemPersistentType
type: Property
summary: Specifies the business class used to persist auditing information in the database.
syntax:
  content: public Type AuditDataItemPersistentType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: The type of a business class used to persist auditing information in the database.
seealso: []
---
To use this property in your code, inherit a custom class from the `AuditDataItemPersistent` class or implement the `IAuditDataItemPersistent<AuditedObjectWeakReferenceType>` interface. Refer to the following example for details.

```csharp
using DevExpress.Xpo;
using DevExpress.Persistent.BaseImpl;

namespace YourSolutionName.Module.BusinessObjects {
    public class AuditDataItemPersistentEx : AuditDataItemPersistent {
        public AuditDataItemPersistentEx(Session session) : base(session) {
        }

        public AuditDataItemPersistentEx(Session session, string userName, DateTime modifiedOn, string description) : base(session, userName, modifiedOn, description) {
        }

        string _myCustomProperty;
        public string MyCustomProperty {
            get {
                return _myCustomProperty;
            }
            set {
                SetPropertyValue(nameof(MyCustomProperty), ref _myCustomProperty, value);
            }
        }

        protected override void OnSaving() {
            base.OnSaving();
            MyCustomProperty = "My custom value";
        }
    }
}
```

The next step is to set this class to `AuditDataItemPersistentType` in the _Startup.cs_ file:

```csharp{7-8}
public void ConfigureServices(IServiceCollection services) {
    // ...    
    services.AddXaf(Configuration, builder => {
        // ...
        builder.UseApplication<YourSolutionName>();
        builder.Modules
            .AddAuditTrailXpo(opt => {
                opt.AuditDataItemPersistentType = typeof(AuditDataItemPersistentEx);
            })
    }
}
```
