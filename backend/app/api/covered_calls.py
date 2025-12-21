from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.covered_call import CoveredCallOut
from app.services.covered_calls import get_covered_calls

