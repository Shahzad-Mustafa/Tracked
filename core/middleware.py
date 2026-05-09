import threading

_SKIP = ('/admin/', '/static/', '/media/', '/summernote/', '/favicon', '/contact/')


def _get_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR', '')
    return xff.split(',')[0].strip() if xff else request.META.get('REMOTE_ADDR', '')


def _parse_ua(ua_string):
    try:
        import user_agents
        ua = user_agents.parse(ua_string)
        if ua.is_mobile:
            device = 'mobile'
        elif ua.is_tablet:
            device = 'tablet'
        elif ua.is_pc:
            device = 'desktop'
        else:
            device = 'other'
        return {
            'browser': ua.browser.family or '',
            'browser_version': ua.browser.version_string or '',
            'os': ua.os.family or '',
            'device_type': device,
        }
    except Exception:
        return {'browser': '', 'browser_version': '', 'os': '', 'device_type': 'other'}


def _record(ip, ua_string, referrer, path, session_key):
    from .models import PageVisit
    info = _parse_ua(ua_string)
    try:
        PageVisit.objects.create(
            ip_address=ip or None,
            user_agent=ua_string[:1000],
            referrer=referrer[:500],
            path=path,
            session_key=session_key,
            **info,
        )
    except Exception:
        pass


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if (
            request.method == 'GET'
            and response.status_code == 200
            and not any(request.path.startswith(s) for s in _SKIP)
        ):
            ip = _get_ip(request)
            ua = request.META.get('HTTP_USER_AGENT', '')
            referrer = request.META.get('HTTP_REFERER', '')
            path = request.path
            session_key = ''
            try:
                if not request.session.session_key:
                    request.session.create()
                session_key = request.session.session_key or ''
            except Exception:
                pass

            # Log in background thread so it never slows down the response
            t = threading.Thread(
                target=_record,
                args=(ip, ua, referrer, path, session_key),
                daemon=True,
            )
            t.start()

        return response
