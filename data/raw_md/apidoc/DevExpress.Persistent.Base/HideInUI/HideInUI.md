---
uid: DevExpress.Persistent.Base.HideInUI
name: HideInUI
type: Enum
summary: Specifies whether a reference property or enumeration value should be hidden on certain UI views.
syntax:
  content: public enum HideInUI
seealso: []
---
You can combine flags to hide a property on select UI views:

```csharp{10}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using System.Collections.ObjectModel;
using System.ComponentModel;

namespace YourSolutionName.Module.BusinessObjects;
[DefaultClassOptions]
public class Category : BaseObject {
   public virtual string Name { get; set; }
   [HideInUI(HideInUI.ListViewColumn | HideInUI.DetailViewEditor)]
   public virtual Guid ParentObjectId { get; set; }
   // ...
}
```

Note that only the following fields are supported for enumeration values:

* `All`
* `DetailView`
* `ListView` 

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace YourSolutionName.Module.BusinessObjects; {
    [DefaultClassOptions]
    public class TestObjects : BaseObject {
        public virtual SampleEnum EnumProperty { get; set; } 
    }

    public enum SampleEnum {
        [HideInUI(HideInUI.All)]
        Value1,
        [HideInUI(HideInUI.DetailView)]
        Value2,
        [HideInUI(HideInUI.ListView)]
        Value3,
        Value4
    } 
}
```