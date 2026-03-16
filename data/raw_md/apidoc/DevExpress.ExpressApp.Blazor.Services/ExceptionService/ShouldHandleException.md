---
uid: DevExpress.ExpressApp.Blazor.Services.ExceptionService.ShouldHandleException(System.Exception)
name: ShouldHandleException(Exception)
type: Method
summary: Specifies how an exception is processed. If you want to process an exception through `IExceptionHandlerService`, override this method and return `true`; if you want to process an exception through `ErrorBoundary` - return `false`.
syntax:
  content: public virtual bool ShouldHandleException(Exception exception)
  parameters:
  - id: exception
    type: System.Exception
    description: A @System.Exception object.
  return:
    type: System.Boolean
    description: '`true` to use `IExceptionHandlerService`; `false` for `ErrorBoundary`.'
seealso: []
---

Override this method to indicate how you want to process an exception. See the following code snippet for an example:

```csharp
using System;
using DevExpress.ExpressApp.Blazor.Services;
using Microsoft.Extensions.Logging;
using DevExpress.ExpressApp;

    public class CustomExceptionHandlerService : ExceptionService {
        public CustomExceptionHandlerService(ILogger<ExceptionService> logger) : base(logger) { 
        }
        public override bool ShouldHandleException(Exception exception) {
            if(exception is MyException) {
                return true;
            }
            else {
                return false;
            }
        }
    }
```