# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.SystemModule;
//...
[DefaultClassOptions]
[ListViewFilter("Today", "GetDate([DueDate]) = LocalDateTimeToday()")]
[ListViewFilter("In three days", @"[DueDate] >= ADDDAYS(LocalDateTimeToday(), -3) AND 
    [DueDate] < LocalDateTimeToday()")]
[ListViewFilter("In two weeks", @"[DueDate] >= ADDDAYS(LocalDateTimeToday(), -14) AND 
    [DueDate] < LocalDateTimeToday()")]
[ListViewFilter("The last week", @"GetDate([DueDate]) > LocalDateTimeLastWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeLastWeek(), 5)")]
[ListViewFilter("This week", @"GetDate([DueDate]) > LocalDateTimeThisWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeThisWeek(), 5)")]
public class Task : BaseObject {
    [ModelDefault("EditMask","d")]
    public virtual DateTime DueDate { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Model;
using DevExpress.ExpressApp.SystemModule;
//...
[DefaultClassOptions]
[ListViewFilter("Today", "GetDate([DueDate]) = LocalDateTimeToday()")]
[ListViewFilter("In three days", @"[DueDate] >= ADDDAYS(LocalDateTimeToday(), -3) AND 
    [DueDate] < LocalDateTimeToday()")]
[ListViewFilter("In two weeks", @"[DueDate] >= ADDDAYS(LocalDateTimeToday(), -14) AND 
    [DueDate] < LocalDateTimeToday()")]
[ListViewFilter("The last week", @"GetDate([DueDate]) > LocalDateTimeLastWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeLastWeek(), 5)")]
[ListViewFilter("This week", @"GetDate([DueDate]) > LocalDateTimeThisWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeThisWeek(), 5)")]
public class Task : BaseObject {
   public Task(Session session) : base(session) {}
   private DateTime dueDate;
   [ModelDefault("EditMask","d")]
   public DateTime DueDate {
      get {
         return dueDate;
      }
      set {
         SetPropertyValue(nameof(DueDate), ref dueDate, value);      }
   }
}
```

# [VB.NET (XPO)](#tab/tabid-vb-xpo)

```vb
Imports DevExpress.ExpressApp.Model
Imports DevExpress.ExpressApp.SystemModule
'...
<DefaultClassOptions>
<ListViewFilter("Today", "GetDate([DueDate]) = LocalDateTimeToday()")>
<ListViewFilter("In three days", "[DueDate] >= ADDDAYS(LocalDateTimeToday(), -3) AND 
    [DueDate] < LocalDateTimeToday()")>
<ListViewFilter("In two weeks", "[DueDate] >= ADDDAYS(LocalDateTimeToday(), -14) AND 
    [DueDate] < LocalDateTimeToday()")>
<ListViewFilter("The last week", "GetDate([DueDate]) > LocalDateTimeLastWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeLastWeek(), 5)")>
<ListViewFilter("This week", "GetDate([DueDate]) > LocalDateTimeThisWeek() AND 
    GetDate([DueDate]) <= ADDDAYS(LocalDateTimeThisWeek(), 5)")>
Public Class Task
      Inherits BaseObject
   Public Sub New(ByVal session As Session)
      MyBase.New(session)
   End Sub
   Private fDueDate As DateTime
   <ModelDefault("EditMask","d")> _
   Public Property DueDate() As DateTime
      Get
         Return fDueDate
      End Get
      Set(ByVal value As DateTime)
         SetPropertyValue(NameOf(DueDate), fDueDate, value)
      End Set
   End Property
End Class
```

***