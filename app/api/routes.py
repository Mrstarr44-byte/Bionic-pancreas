# app/api/routes.py

from flask import jsonify, request
from flask_login import login_required, current_user
from app.api import bp
from app import db
from app.models import SimulationLog
from sqlalchemy import select, desc

@bp.route('/simulations', methods=['GET'])
@login_required
def get_simulations():
    """Return the logged‑in user's simulation logs with pagination.
    Query parameters:
        page – page number (default 1)
        per_page – items per page (default 10)
    """
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
    except Exception:
        return jsonify({"status": "error", "message": "Invalid pagination parameters"}), 400

    stmt = (
        select(SimulationLog)
        .where(SimulationLog.user_id == current_user.id)
        .order_by(desc(SimulationLog.timestamp))
    )

    pagination = db.paginate(stmt, page=page, per_page=per_page, error_out=False)
    logs = pagination.items

    data = [
        {
            "id": log.id,
            "glucose_before": log.glucose_before,
            "glucose_after": log.glucose_after,
            "carbs": getattr(log, "carbs", None),
            "insulin": getattr(log, "insulin", None),
            "status": getattr(log, "status", None),
            "timestamp": log.timestamp.isoformat() if log.timestamp else None,
        }
        for log in logs
    ]

    return jsonify({
        "status": "success",
        "data": data,
        "pagination": {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
        },
    })
