---
uid: DevExpress.ExpressApp.Win.WinWindow.QueryDefaultFormIcon
name: QueryDefaultFormIcon
type: Event
summary: Occurs before assigning default icons to the [](xref:DevExpress.ExpressApp.Win.WinWindow)'s Template.
syntax:
  content: public static event EventHandler<QueryIconEventArgs> QueryDefaultFormIcon
seealso: []
---
By default, the [QueryIconEventArgs.IconLarge](xref:DevExpress.ExpressApp.Win.QueryIconEventArgs.IconLarge) and [QueryIconEventArgs.IconSmall](xref:DevExpress.ExpressApp.Win.QueryIconEventArgs.IconSmall) properties contain default icons extracted from the application's executable file. However, you can handle this event to specify custom default icons that should be used by Windows in a Windows Forms application. You can handle this event, for instance, in the **Main** method of your **Program** class.

_Program.cs_

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
public class Program {
    static Icon smallIcon;
    static Icon largeIcon;
    //...
    public static void Main(string[] arguments) {
        //...
        WinWindow.QueryDefaultFormIcon += WinWindow_QueryDefaultFormIcon;
        winApplication.Setup();
        winApplication.Start();
    }
    static void WinWindow_QueryDefaultFormIcon(object sender, QueryIconEventArgs e) {
        if (smallIcon == null)
            smallIcon = Icon.ExtractAssociatedIcon("C:\\MyIcon.ico");
        if(largeIcon == null)
            largeIcon = Icon.ExtractAssociatedIcon("C:\\MyIcon2.ico");
        e.IconLarge = largeIcon;
        e.IconSmall = smallIcon;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Drawing
'...
Public Class Program
    Private Shared smallIcon As Icon
    Private Shared largeIcon As Icon
    '...
    Public Shared Sub Main(ByVal arguments() As String)
        '...
        AddHandler WinWindow.QueryDefaultFormIcon, AddressOf WinWindow_QueryDefaultFormIcon
        winApplication.Setup()
        winApplication.Start()
    End Sub
    Private Shared Sub WinWindow_QueryDefaultFormIcon(ByVal sender As Object, _
    ByVal e As QueryIconEventArgs)
        If smallIcon Is Nothing Then
            smallIcon = Icon.ExtractAssociatedIcon("C:\MyIcon.ico")
        End If
        If largeIcon Is Nothing Then
            largeIcon = Icon.ExtractAssociatedIcon("C:\MyIcon2.ico")
        End If
        e.IconLarge = largeIcon
        e.IconSmall = smallIcon
    End Sub
End Class
```

***