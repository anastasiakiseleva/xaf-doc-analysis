# [CS\MainDemo.Module\BusinessObjects\Department.cs](#tab/tabid-module)
```csharp{5}
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Module.BusinessObjects;

[OptimisticLockIgnore]
public class Department : BaseObject {
    //...
}
```
***