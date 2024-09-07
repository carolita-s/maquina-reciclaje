SELECT * FROM MaquinaReciclaje;
SELECT nombre FROM MaquinaReciclaje WHERE capacidad > 1000;
SELECT COUNT(*) FROM MaquinaReciclaje;
SELECT AVG(capacidad) FROM MaquinaReciclaje;
SELECT nombre, capacidad FROM MaquinaReciclaje ORDER BY capacidad DESC;
