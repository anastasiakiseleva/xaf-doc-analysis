---
uid: "118451"
seealso: []
title: 'How to: Show Various Notifications to Multiple Users'
---
# How to: Show Various Notifications to Multiple Users

When you implement [notifications](xref:113688) in your application, XAF creates a instance of the notification class and displays it to each user. If one user interacts with this notification (for example, invokes **Snooze** or **Dismiss** Actions), XAF propagates modifications for all users. This topic explains how to create different notifications for multiple users to allow them to use Actions without collisions.

1. Assume that you have an application with the [Security System](xref:113366) enabled. The `MyNotification` class implements the [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) interface and exposes the `AssignedTo` and `MyTask` properties.

    # [Entity Framework Core](#tab/tabid-efcore)
    ```csharp
    using System;
    using System.ComponentModel;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using DevExpress.Persistent.Base.General;
    using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
    using DevExpress.Persistent.BaseImpl.EF;
    
    namespace MySolution.Module.BusinessObjects;
    public class MyNotification : BaseObject, ISupportNotifications {
        public virtual MyTask MyTask { get; set; }
        public virtual ApplicationUser AssignedTo { get; set; }
        private DateTime? alarmTime;
        public virtual DateTime? AlarmTime {
            get {
                return alarmTime;
            }
            set {
                alarmTime = value;
                if (value == null) {
                    IsPostponed = false;
                }
            }
        }
        [Browsable(false), NotMapped]
        public object UniqueId {
            get { return ID; }
        }
        [Browsable(false)]
        public virtual bool IsPostponed { get; set; }
        [Browsable(false)]
        public virtual string NotificationMessage { get { return MyTask.Subject; } }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [XPO](#tab/tabid-xpo)
    ```csharp
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.ComponentModel;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;
    using DevExpress.Persistent.Base.General;
    using DevExpress.Persistent.BaseImpl;
    using DevExpress.Xpo;

    namespace MySolution.Module.BusinessObjects;
    public class MyNotification : BaseObject, ISupportNotifications {
        public MyNotification(Session session):base(session) { }
        [Association("MyTask-MyNotifications")]
        public MyTask MyTask {
            get {
                return GetPropertyValue<MyTask>(nameof(MyTask));
            }
            set {
                SetPropertyValue(nameof(MyTask), value);
            }
        }
        [Association("AssignedTo-MyNotifications")]
        public ApplicationUser AssignedTo {
            get {
                return GetPropertyValue<ApplicationUser>(nameof(AssignedTo));
            }
            set {
                SetPropertyValue(nameof(AssignedTo), value);
            }
        }
        #region ISupportNotifications members
        private DateTime? alarmTime;
        public DateTime? AlarmTime {
            get { return alarmTime; }
            set {
                if(value == null) {
                    IsPostponed = false;
                }
                SetPropertyValue(nameof(AlarmTime), ref alarmTime, value);
            }
        }

        [Browsable(false)]
        public bool IsPostponed {
            get {
                return GetPropertyValue<bool>(nameof(IsPostponed));
            }
            set {
                SetPropertyValue(nameof(IsPostponed), value);
            }
        }

        [Browsable(false)]
        public string NotificationMessage {
            get { return MyTask.Subject; }
        }

        public object UniqueId {
            get {
                return Oid;
            }
        }
        #endregion ISupportNotifications members
    }
    ```
    ***

2. The `MyTask` property is an object of the custom `MyTask` type. The `MyTask` class has the `MyNotifications` aggregated collection of notifications that is a part of the [one-to-many relationship](xref:402958).

    # [Entity Framework Core](#tab/tabid-efcore)
    ```csharp
    using DevExpress.Persistent.Base;
    using DevExpress.Persistent.BaseImpl.EF;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.Collections.ObjectModel;

    namespace MySolution.Module.BusinessObjects;
    [DefaultClassOptions]
    public class MyTask : BaseObject {
        public virtual string Subject { get; set; }
        [DevExpress.ExpressApp.DC.Aggregated]
        public virtual IList<MyNotification> MyNotifications { get; set; } = new ObservableCollection<MyNotification>();
    }
    ```
    
    # [XPO](#tab/tabid-xpo)
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
    public class MyTask : BaseObject {
        public MyTask(Session session) : base(session) {
        }
        public string Subject {
            get {
                return GetPropertyValue<string>(nameof(Subject));
            }
            set {
                SetPropertyValue(nameof(Subject), value);
            }
        }
        [Association("MyTask-MyNotifications")]
        public XPCollection<MyNotification> MyNotifications {
            get {
                return GetCollection<MyNotification>(nameof(MyNotifications));
            }
        }
    }
    ```
    ***

    > [!NOTE]
    > You may use the `Event` class from the Business Class Library with the [Scheduler Module](xref:112811) instead of the custom [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) object. If you do so, Scheduler capabilities will not work (for example, the [](xref:DevExpress.XtraScheduler.RecurringReminder) functionality). To avoid this, you should create a separate `Event` instance for each user.

3. Navigate to the _YourApplicationName.Module\YourApplicationNameModule.cs_ file. In the overridden [ModuleBase.Setup](xref:DevExpress.ExpressApp.ModuleBase.Setup*) method, subscribe to the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event. Get the [](xref:DevExpress.ExpressApp.Notifications.NotificationsModule) instance and subscribe to the [DefaultNotificationsProvider.CustomizeNotificationCollectionCriteria](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider.CustomizeNotificationCollectionCriteria) event.

    ```csharp
    using DevExpress.Data.Filtering;
    using DevExpress.ExpressApp.Notifications;
    using DevExpress.Persistent.Base.General;
    // ...
    public override void Setup(XafApplication application) {
        base.Setup(application);
        application.LoggedOn += application_LoggedOn;
    }
    void application_LoggedOn(object sender, LogonEventArgs e) {
        NotificationsModule notificationsModule = Application.Modules.FindModule<NotificationsModule>();
        DefaultNotificationsProvider notificationsProvider = notificationsModule.DefaultNotificationsProvider;
        notificationsProvider.CustomizeNotificationCollectionCriteria +=
        notificationsProvider_CustomizeNotificationCollectionCriteria;
    }
    void notificationsProvider_CustomizeNotificationCollectionCriteria(
        object sender, CustomizeCollectionCriteriaEventArgs e) {
        if (e.Type == typeof(MyNotification)) {
            e.Criteria = CriteriaOperator.FromLambda(x => x.AssignedTo == null || x.AssignedTo.ID == (Guid)CurrentUserIdOperator.CurrentUserId());
        }
    }
    ```

As a result, XAF filters notifications based on the assigned user if you specify the `AssignedTo` property or displays the same notifications for all users if the `AssignedTo` value is empty.

![XAF ASP.NET Core Blazor, Notification for Admin, DevExpress](~/images/notificationforadmin128379.png)

![XAF ASP.NET Core Blazor, Notification for User, DevExpress](~/images/notificationforuser128378.png)

If you want to open the corresponding `MyTask` Detail View with a double click on a notification in the notification window, create a [Controller](xref:112621) that inherits from `WinNotificationsMessageListViewController` in a WinForms application.

>[!NOTE]
>This functionality is not available in XAF ASP.NET Core Blazor applications.

The following code snippet demonstrates the Controller implementation for a Windows Forms application:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Notifications.Win;
using YourApplicationName.Module.BusinessObjects;

namespace YourApplicationName.Win.Controllers;

public class MyWinNotificationsMessageListViewController : WinNotificationsMessageListViewController {
    protected override DevExpress.ExpressApp.View CreateDetailView() {
        Object obj = ViewCurrentObject.NotificationSource;
        if (ViewCurrentObject.NotificationSource is MyNotification) {
            obj = ((MyNotification)ViewCurrentObject.NotificationSource).MyTask;
        }
        IObjectSpace objectSpace = Application.CreateObjectSpace(obj.GetType());
        Object objectInTargetObjectSpace = objectSpace.GetObject(obj);
        DevExpress.ExpressApp.View view = Application.CreateDetailView(objectSpace, objectInTargetObjectSpace);
        ProcessDetailView(view);
        return view;
    }
}
```

![XAF Windows Forms, Open Detail View from Notification Window, DevExpress](~/images/notificationwindow_taskdetailview128382.png)

If you need to delete a notification when a user dismisses it, create a new [](xref:DevExpress.ExpressApp.ObjectViewController`2):

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Notifications;
using DevExpress.Persistent.Base.General;
//...
public class DeleteOnDismissController : ObjectViewController<DetailView, NotificationsObject> {
    private NotificationsService service;
    protected override void OnActivated() {
        base.OnActivated();
        service = Application.Modules.FindModule<NotificationsModule>().NotificationsService;
        NotificationsDialogViewController notificationsDialogViewController = 
Frame.GetController<NotificationsDialogViewController>();
        if (service != null && notificationsDialogViewController != null) {
            notificationsDialogViewController.Dismiss.Executing += Dismiss_Executing;
            notificationsDialogViewController.Dismiss.Executed += Dismiss_Executed;
        }
    }
    protected override void OnDeactivated() {
        NotificationsDialogViewController notificationsDialogViewController = 
Frame.GetController<NotificationsDialogViewController>();
        if(notificationsDialogViewController != null) {
            notificationsDialogViewController.Dismiss.Executing -= Dismiss_Executing;
            notificationsDialogViewController.Dismiss.Executed -= Dismiss_Executed;
        }
        base.OnDeactivated();
    }
    private void Dismiss_Executing(object sender, System.ComponentModel.CancelEventArgs e) {
        service.ItemsProcessed += Service_ItemsProcessed;
    }
    private void Service_ItemsProcessed(object sender, 
DevExpress.Persistent.Base.General.NotificationItemsEventArgs e) {
        IObjectSpace space = Application.CreateObjectSpace(typeof(MyNotification));
        foreach(INotificationItem item in e.NotificationItems) {
            if(item.NotificationSource is MyNotification) {
                space.Delete(space.GetObject(item.NotificationSource));
            }
        }
        space.CommitChanges();
    }
    private void Dismiss_Executed(object sender, 
DevExpress.ExpressApp.Actions.ActionBaseEventArgs e) {
        service.ItemsProcessed -= Service_ItemsProcessed;
    }
}
```
