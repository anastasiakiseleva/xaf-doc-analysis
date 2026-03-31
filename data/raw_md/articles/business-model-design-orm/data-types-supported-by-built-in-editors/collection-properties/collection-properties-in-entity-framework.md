---
uid: "113570"
title: Collection Properties in EF Core
seealso:  
- linkId: "117395"
- linkId: "404862"
- linkId: "404429"
---
# Collection Properties in EF Core

The example below illustrates how to implement [Collection Properties](xref:113568) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.ObjectModel;

namespace DXApplication21.Module.BusinessObjects {
    [DefaultClassOptions]
    public class Employee : BaseObject {
        // ...
        // An associated collection - Tasks can be linked to and unlinked from an Employee object.
        public virtual IList<Task> Tasks { get; set; } = new ObservableCollection<Task>();
        // An aggregated collection - Addresses are a part of an Employee object
        // and cannot exist without this object.
        [Aggregated]
        public virtual IList<Address> Addresses { get; set; } = new ObservableCollection<Address>();
    }
}
```

***

> [!IMPORTANT]
> [!include[inotifycollectionchanged-note](~/templates/inotifycollectionchanged-note.md)]

Note that collection properties should be declared as _virtual_ in EF Core.