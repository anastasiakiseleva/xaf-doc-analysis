---
uid: "113689"
seealso:
- linkId: "113687"
- linkId: "113696"
title: 'How to: Use Notifications with a Custom Business Class (Implement ISupportNotifications)'
owner: Anastasiya Kisialeva
---
# How to: Use Notifications with a Custom Business Class (Implement ISupportNotifications)

This example demonstrates how to associate [Notifications](xref:113688) with a custom business class.

Assume you have the following `MyTask` business class.

# [Entity Framework Core](#tab/tabid-efcore)
```csharp
using System;
using System.Collections.Generic;
using System.ComponentModel;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions]
 public class MyTask : BaseObject {
    public virtual string Subject { get; set; }
    public virtual DateTime DueDate { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
# [XPO](#tab/tabid-xpo)
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;

namespace MySolution.Module.BusinessObjects;
[DefaultClassOptions]
public class MyTask : BaseObject {
	public MyTask(Session session) : base(session) { }
	public string Subject {
		get {
			return GetPropertyValue<string>(nameof(Subject));
		}
		set {
			SetPropertyValue(nameof(Subject), value);
		}
	}
	public DateTime DueDate {
		get {
			return GetPropertyValue<DateTime>(nameof(DueDate));
		}
		set {
			SetPropertyValue(nameof(DueDate), value);
		}
	}
}
```
***

The goal is to use the functionality of the Notifications module to send a reminder to a user before the `DueDate`.

1. [Add the Notifications module to your application](xref:113690#add-the-notifications-module-to-your-application).
	
	> [!NOTE]
	> The default notification refresh interval is 5 minutes, but you can reduce this interval for testing purposes. For more information, refer to the following topic: [How to Specify the Notification Refresh Frequency](xref:113690#how-to-specify-the-notification-refresh-frequency)
2. Implement the [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) interface in the `MyTask` class.

	# [Entity Framework Core](#tab/tabid-efcore)
	```csharp
    using DevExpress.Persistent.Base.General;
	using DevExpress.Persistent.BaseImpl.EF;
	// ...
	[DefaultClassOptions]
	public class MyTask : BaseObject, ISupportNotifications {
        // ...
	    #region ISupportNotifications members
        private DateTime? alarmTime;
	    [Browsable(false)]
	    public virtual DateTime? AlarmTime { 
	        get { return alarmTime; }
	        set {
	            if (value == null) {
	                RemindIn = null;
	                IsPostponed = false;
	            }
				alarmTime = value;
	        }
        }

	    [Browsable(false)]
	    public virtual bool IsPostponed { get; set; }

	    [Browsable(false),NotMapped]
	    public string NotificationMessage {
	        get { return Subject; }
	    }
	    public virtual TimeSpan? RemindIn { get; set; }

	    [Browsable(false),NotMapped]
	    public object UniqueId {
	        get { return ID; }
	    }
	    #endregion
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
	using DevExpress.Persistent.Base;
	using DevExpress.Persistent.Base.General;
	using DevExpress.Persistent.BaseImpl;
	using DevExpress.Xpo;

	namespace MySolution.Module.BusinessObjects;
	[DefaultClassOptions]
	public class MyTask : BaseObject, ISupportNotifications {

		#region ISupportNotifications members
		private DateTime? alarmTime;
		[Browsable(false)]
		public DateTime? AlarmTime {
			get { return alarmTime; }
			set {
				if(value == null) {
					RemindIn = null;
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
			get { return Subject; }
		}
		public TimeSpan? RemindIn {
			get {
				return GetPropertyValue<TimeSpan?>(nameof(RemindIn));
			}
			set {
				SetPropertyValue(nameof(RemindIn), value);
			}
		}

		[Browsable(false)]
		public object UniqueId {
			get { return Oid; }
		}
		#endregion
	}
	```
	***
3. Override the `OnSaving` method to initialize `AlarmTime` based on the `RemindIn` interval specified by a user.
	
	# [Entity Framework Core](#tab/tabid-efcore)
	```csharp
	using DevExpress.ExpressApp;
	// ...
	[DefaultClassOptions]
	public class MyTask : BaseObject, ISupportNotifications {
	    // ...
	    #region IXafEntityObject members
	    public override void OnSaving() {
	        if(RemindIn.HasValue) {
	            if((AlarmTime == null) || (AlarmTime < DueDate - RemindIn.Value)) {
	                AlarmTime = DueDate - RemindIn.Value;
	            }
	        }
	        else {
	            AlarmTime = null;
	        }
	        if (AlarmTime == null) {
	            RemindIn = null;
	            IsPostponed = false;
	        }
	    }
	    #endregion
	}

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
	```
	# [XPO](#tab/tabid-xpo)
	```csharp
	// ...
	using DevExpress.Xpo;

	namespace MySolution.Module.BusinessObjects;
	[DefaultClassOptions]
	public class MyTask : BaseObject, ISupportNotifications {
		// ...
        protected override void OnSaving() {
            base.OnSaving();
            if(RemindIn.HasValue) {
                if((AlarmTime == null) || (AlarmTime < DueDate - RemindIn.Value)) {
                    AlarmTime = DueDate - RemindIn.Value;
                }
            }
            else {
                AlarmTime = null;
            }
            if(AlarmTime == null) {
                RemindIn = null;
                IsPostponed = false;
            }
        }
	}
	```
	***

4. Run the application and create a new overdue task in the past (the `DueDate` should be earlier than the current time). Specify a non-empty value for the `RemindIn` property that defines the time between the notification alert and the `DueDate` moment (an empty `RemindIn` value means that the alert is never displayed).

	![|XAF ASP.NET Core Blazor, Notifications Enabled in Custom Class, DevExpress](~/images/notifications_customclass117576.png)

5. Save the task. The Notifications window should appear after the time span specified in the [NotificationsOptionsBase.NotificationsRefreshInterval](xref:DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.NotificationsRefreshInterval) property or sooner.

	![XAF ASP.NET Core Blazor, Notifications Window  in Custom Class, DevExpress](~/images/howto_reminders_5117565.png)
