# [CS\MainDemo.Module\BusinessObjects\Department.cs](#tab/tabid-module)
```csharp{5}
using Microsoft.EntityFrameworkCore;

namespace MainDemo.Module.BusinessObjects;

[OptimisticLock(OptimisticLockDetection = OptimisticLockDetection.AllFields,OptimisticLockHandling = OptimisticLockHandling.Reload)]
public class Department : BaseObject, ITreeNode {
    //...
}
```
***