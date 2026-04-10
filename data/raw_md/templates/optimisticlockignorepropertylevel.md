# [CS\MainDemo.Module\BusinessObjects\Department.cs](#tab/tabid-module)
```csharp{7}
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Module.BusinessObjects;

public class Department : BaseObject {
    //...
    [OptimisticLockIgnore]
    public virtual string Office { get; set; }
}
```
***