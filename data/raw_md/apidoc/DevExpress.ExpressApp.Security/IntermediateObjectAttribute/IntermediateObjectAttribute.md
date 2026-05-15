---
uid: DevExpress.ExpressApp.Security.IntermediateObjectAttribute
name: IntermediateObjectAttribute
type: Class
summary: Applies to classes. Marks the class as an intermediate in the [many-to-many relationship](xref:112654#technique-2-with-an-intermediate-object) declared with @DevExpress.Xpo.ManyToManyAliasAttribute.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class)]
    public class IntermediateObjectAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Security.IntermediateObjectAttribute._members
  altText: IntermediateObjectAttribute Members
---
The following example demonstrates how to apply this attribute:

# [C#](#tab/tabid-csharp)

```csharp{31}
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using DevExpress.Xpo;
using System.Collections.Generic;
using System.ComponentModel;
// ...
[DefaultClassOptions]
public class Contact : XPObject {
    // ...
    [Browsable(false)]
    [Association("Contact-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Task))]
    public IList<Task> TaskCollection {
        get { return GetList<Task>(nameof(TaskCollection)); }
    }
}
[DefaultClassOptions]
public class Task : XPObject {
    // ...
    [Browsable(false)]
    [Association("Task-ContactTasks"), Aggregated]
    public XPCollection<ContactTask> ContactTasks { 
        get { return GetCollection<ContactTask>(nameof(ContactTasks)); } }
    [ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Contact))]
    public IList<Contact> ContactCollection {
        get { return GetList<Contact>(nameof(ContactCollection)); }
    }
}
[IntermediateObject(nameof(Contact), nameof(Task))]
public class ContactTask : XPObject {
    public ContactTask(Session session) : base(session) { }
    Contact fContact;
    [Association("Contact-ContactTasks")]
    public Contact Contact {
        get { return fContact; }
        set { SetPropertyValue<Contact>(nameof(Contact), ref fContact, value); }
    }
    Task fTask;
    [Association("Task-ContactTasks")]
    public Task Task {
        get { return fTask; }
        set { SetPropertyValue<Task>(nameof(Task), ref fTask, value); }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb{41}
Imports DevExpress.ExpressApp.Security
Imports DevExpress.Persistent.Base
Imports DevExpress.Xpo
Imports System.Collections.Generic
Imports System.ComponentModel
' ...
<DefaultClassOptions>
Public Class Contact
    Inherits XPObject
    ' ...
    <Browsable(False), Association("Contact-ContactTasks"), Aggregated>
    Public ReadOnly Property ContactTasks() As XPCollection(Of ContactTask)
        Get
            Return GetCollection(Of ContactTask)(NameOf(ContactTasks))
        End Get
    End Property
    <ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Task))>
    Public ReadOnly Property TaskCollection() As IList(Of Task)
        Get
            Return GetList(Of Task)(NameOf(TaskCollection))
        End Get
    End Property
End Class
<DefaultClassOptions>
Public Class Task
    Inherits XPObject
    ' ...
    <Browsable(False), Association("Task-ContactTasks"), Aggregated>
    Public ReadOnly Property ContactTasks() As XPCollection(Of ContactTask)
        Get
            Return GetCollection(Of ContactTask)(NameOf(ContactTasks))
        End Get
    End Property
    <ManyToManyAlias(nameof(ContactTasks), nameof(ContactTask.Contact))>
    Public ReadOnly Property ContactCollection() As IList(Of Contact)
        Get
            Return GetList(Of Contact)(NameOf(ContactCollection))
        End Get
    End Property
End Class
<IntermediateObject(nameof(Contact), nameof(Task))>
Public Class ContactTask
    Inherits XPObject
    Public Sub New(ByVal session As Session)
        MyBase.New(session)
    End Sub
    Private fContact As Contact
    <Association("Contact-ContactTasks")>
    Public Property Contact() As Contact
        Get
            Return fContact
        End Get
        Set(ByVal value As Contact)
            SetPropertyValue(Of Contact)(NameOf(Contact), fContact, value)
        End Set
    End Property
    Private fTask As Task
    <Association("Task-ContactTasks")>
    Public Property Task() As Task
        Get
            Return fTask
        End Get
        Set(ByVal value As Task)
            SetPropertyValue(Of Task)(NameOf(Task), fTask, value)
        End Set
    End Property
End Class
```
***