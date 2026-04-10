The following code snippet demonstrates how to initialize the **Address1** reference property with a new or existing object:

**File**: _MySolution.Module\BusinessObjects\Employee.cs_


```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace YourSolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class Employee : IXafEntityObject {
    [Key]
    public virtual Guid ID { get; set; }

    public virtual string Manager { get; set; }
    public void OnCreated() {
        // ...
        var address = ObjectSpace.FindObject<Address>(CriteriaOperator.FromLambda<Address>(a => a.Country == "USA"));
        if(address == null) {
            address = ObjectSpace.CreateObject<Address>();
            address.Country = "USA";
        }
        Address1 = address;
    }
    public virtual Address Address1 { get; set; }
    public void OnLoaded() { }
    public void OnSaving() { }
    public IObjectSpace ObjectSpace {
        get {
            return ((IObjectSpaceLink)this).ObjectSpace;
        }
    }
}
[DefaultClassOptions]
[DefaultProperty(nameof(Country))]
public class Address : BaseObject {
    public virtual string Country { get; set; }
    // ...
}
// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

Alternatively, you can inherit your class from the **DevExpress.Persistent.BaseImpl.EF.BaseObject** class as follows:

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace YourSolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class Employee : BaseObject {
    public virtual string Manager { get; set; }
    public override void OnCreated() {
        // ...
        var address = ObjectSpace.FindObject<Address>(CriteriaOperator.FromLambda<Address>(a => a.Country == "USA"));
        if(address == null) {
            address = ObjectSpace.CreateObject<Address>();
            address.Country = "USA";
        }
        Address1 = address;
    }
    public virtual Address Address1 { get; set; }

}
[DefaultClassOptions]
[DefaultProperty(nameof(Country))]
public class Address : BaseObject {
    public virtual string Country { get; set; }
    // ...
}


// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
