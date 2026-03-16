---
uid: "113696"
seealso: []
title: 'How to: Show Notifications to a Specific User'
owner: Anastasiya Kisialeva
---
# How to: Show Notifications to a Specific User

XAF displays [notifications](xref:113688) for all users by default. This example demonstrates how to filter notifications to display the [Notifications window](xref:113692) only to a specific user.

For instance, you have an [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) business object that exposes the `AssignedTo` property. You can refer to the following topic for an example of the class implementation: [How to: Use Notifications with a Custom Business Class (Implement ISupportNotifications)](xref:113689).

# [C# (EF Core)](#tab/tabid-efcore)
```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.Generic;
using System.ComponentModel;
using System.Collections.ObjectModel;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions]
public class MyTask : BaseObject, ISupportNotifications {
    // ...
    public virtual ApplicationUser AssignedTo { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-xpo)
```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System.Collections.ObjectModel;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions]
public class MyTask : BaseObject, ISupportNotifications {
    // ...
    [Association("AssignedTo-MyTasks")]
    public ApplicationUser AssignedTo {
        get {
            return GetPropertyValue<ApplicationUser>(nameof(AssignedTo));
        }
        set {
            SetPropertyValue(nameof(AssignedTo), value);
        }
    }
}
```
***

The `ApplicationUser` is a [custom Security System user type](xref:113384) that has the One-to-Many relationship with `Tasks`.

# [C# (EF Core)](#tab/tabid-efcore)
```csharp
using System.ComponentModel;
using System.Collections.ObjectModel;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions, DefaultProperty(nameof(UserName))]
public class ApplicationUser : PermissionPolicyUser {
    // ...
    public virtual IList<MyTask> MyTasks { get; set; } = new ObservableCollection<MyTask>();
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-xpo)
```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using System.Collections.ObjectModel;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions, DefaultProperty(nameof(UserName))]
public class ApplicationUser : PermissionPolicyUser {
    // ...
    [Association("AssignedTo-MyTasks")]
    public XPCollection<MyTask> MyTasks { get { return GetCollection<MyTask>(nameof(MyTasks)); } }
}
```
***

Navigate to the _YourApplicationName.Module\Module.cs_ file. In the overridden [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method, subscribe to the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event. In this event handler, get the [](xref:DevExpress.ExpressApp.Notifications.NotificationsModule) instance and subscribe to the [DefaultNotificationsProvider.CustomizeNotificationCollectionCriteria](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider.CustomizeNotificationCollectionCriteria) event.

# [C# (EF Core)](#tab/tabid-efcore)
```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.Notifications;
using DevExpress.Persistent.Base.General;

namespace MySolution.Module;
public sealed class MainDemoModule : ModuleBase {
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.LoggedOn += application_LoggedOn;
    }
    void application_LoggedOn(object sender, LogonEventArgs e) {
        NotificationsModule notificationsModule = Application.Modules.FindModule<NotificationsModule>();
        DefaultNotificationsProvider notificationsProvider = notificationsModule.DefaultNotificationsProvider;
        notificationsProvider.CustomizeNotificationCollectionCriteria += notificationsProvider_CustomizeNotificationCollectionCriteria;
    }
    void notificationsProvider_CustomizeNotificationCollectionCriteria(
        object sender, CustomizeCollectionCriteriaEventArgs e) {
        if(e.Type == typeof(MyTask)) {
            e.Criteria = CriteriaOperator.FromLambda<MyTask>(x => x.AssignedTo == null || x.AssignedTo.ID == (Guid)CurrentUserIdOperator.CurrentUserId());
        }
    }
}
```

# [C# (XPO)](#tab/tabid-xpo)
```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.Notifications;
using DevExpress.Persistent.Base.General;

namespace MySolution.Module;
public sealed class MainDemoModule : ModuleBase {
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.LoggedOn += application_LoggedOn;
    }
    void application_LoggedOn(object sender, LogonEventArgs e) {
        NotificationsModule notificationsModule = Application.Modules.FindModule<NotificationsModule>();
        DefaultNotificationsProvider notificationsProvider = notificationsModule.DefaultNotificationsProvider;
        notificationsProvider.CustomizeNotificationCollectionCriteria += notificationsProvider_CustomizeNotificationCollectionCriteria;
    }
    void notificationsProvider_CustomizeNotificationCollectionCriteria(
        object sender, CustomizeCollectionCriteriaEventArgs e) {
        if(e.Type == typeof(MyTask)) {
            e.Criteria = CriteriaOperator.FromLambda<MyTask>(x => x.AssignedTo == null || x.AssignedTo.Oid == (Guid)CurrentUserIdOperator.CurrentUserId());
        }
    }
}
```
***

As a result, XAF displays a notification only if the `AssignedTo` property's value is empty or refers to the current user.

> [!NOTE]
> A user must have security permissions for the `ISuppportNotifications` objects in order to see them.

If you [use the scheduler event descendant](xref:113687) instead of a custom @DevExpress.Persistent.Base.General.ISupportNotifications object, access the @DevExpress.ExpressApp.Scheduler.NotificationsProvider object and handle the [NotificationsProvider.CustomizeNotificationCollectionCriteria](xref:DevExpress.ExpressApp.Scheduler.NotificationsProvider.CustomizeNotificationCollectionCriteria) event.

```csharp
using DevExpress.ExpressApp.Scheduler;
// ...
void application_LoggedOn(object sender, LogonEventArgs e) {
    SchedulerModuleBase schedulerModule = Application.Modules.FindModule<SchedulerModuleBase>();
    ISchedulerNotificationsProvider notificationsProvider = schedulerModule.NotificationsProvider;
    notificationsProvider.CustomizeNotificationCollectionCriteria += notificationsProvider_CustomizeNotificationCollectionCriteria;
}
```


In ASP.NET Core Blazor applications, use @DevExpress.ExpressApp.Scheduler.Blazor.SchedulerBlazorModule:
    
```csharp
using DevExpress.ExpressApp.Scheduler;
// ...
void application_LoggedOn(object sender, LogonEventArgs e) {
    SchedulerModuleBase schedulerModule = Application.Modules.FindModule<SchedulerBlazorModule>();
    ISchedulerNotificationsProvider notificationsProvider = schedulerModule.NotificationsProvider;
    notificationsProvider.CustomizeNotificationCollectionCriteria += notificationsProvider_CustomizeNotificationCollectionCriteria;
}
```
